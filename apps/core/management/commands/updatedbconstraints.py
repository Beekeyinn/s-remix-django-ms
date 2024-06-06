from django.core.management.base import BaseCommand
from django.db import connection


def get_dictionary_from_cursor(cursor):
    desc = cursor.description
    return [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]


def get_tables_from_schema(schema="django"):
    with connection.cursor() as cursor:
        cursor.execute(
            f"""SELECT table_name FROM information_schema.tables WHERE table_schema = '{schema}'"""
        )
        tables = get_dictionary_from_cursor(cursor)
    return tables


def get_constraints_from_table(table_name, schema="django"):
    with connection.cursor() as cursor:
        cursor.execute(
            f"""SELECT
    cons.conname AS constraint_name,
    cons.contype AS constraint_type,
    att1.attname AS constraint_field,
    cl.relname AS table_name,
    att2.attname AS reference_field,
    cl_ref_schema.nspname AS reference_table_schema,
    cl_ref.relname AS reference_table_name
FROM
    pg_catalog.pg_constraint cons
JOIN
    pg_catalog.pg_class cl ON cl.oid = cons.conrelid
JOIN
    pg_catalog.pg_namespace cl_schema ON cl_schema.oid = cl.relnamespace
JOIN
    pg_catalog.pg_attribute att1 ON att1.attrelid = cl.oid AND att1.attnum = ANY(cons.conkey)
JOIN
    pg_catalog.pg_class cl_ref ON cl_ref.oid = cons.confrelid
JOIN
    pg_catalog.pg_namespace cl_ref_schema ON cl_ref_schema.oid = cl_ref.relnamespace
JOIN
    pg_catalog.pg_attribute att2 ON att2.attrelid = cons.confrelid AND att2.attnum = ANY(cons.confkey)
WHERE
    cl.relname = '{table_name}' AND
    cons.contype = 'f';"""
        )
        constraints = get_dictionary_from_cursor(cursor)
    return constraints


def delete_and_update_constraints(constraints):
    with connection.cursor() as cursor:
        for constraint in constraints:
            print(
                f"Updating constraint: {constraint['constraint_name']} from table: {constraint['table_name']} with reference table: {constraint['reference_table_name']}"
            )
            drop_query = f"""ALTER TABLE django.{constraint['table_name']} DROP CONSTRAINT "{constraint['constraint_name']}";"""
            update_query = f"""ALTER TABLE django.{constraint['table_name']} ADD CONSTRAINT {constraint['constraint_name']} FOREIGN KEY ({constraint['constraint_field']}) REFERENCES {constraint['reference_table_schema']}."{constraint['reference_table_name']}"({constraint['reference_field']}) ON DELETE CASCADE ON UPDATE CASCADE DEFERRABLE INITIALLY DEFERRED;"""
            cursor.execute(drop_query + update_query)


class Command(BaseCommand):
    help = "Update foreign key constraints on_delete behavior in the database."

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            tables = get_tables_from_schema()
            result = {}
            for table in tables:
                print("updating table:", table["table_name"])
                constraints = get_constraints_from_table(table["table_name"])
                result[table["table_name"]] = constraints
                delete_and_update_constraints(constraints)
            # print(json.dumps(result, indent=4))
