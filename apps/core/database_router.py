class DjangoAppRouter:

    def db_for_read(self, model, **hints):

        if "remix" not in model._meta.app_label:
            return "default"
        return None

    def db_for_write(self, model, **hints):

        if "remix" not in model._meta.app_label:
            return "default"
        return None

    def allow_relation(self, obj1, obj2, **hints):

        if "remix" not in obj1._meta.app_label or "remix" not in obj2._meta.app_label:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):

        if "remix" not in app_label:
            return db == "default"
        return None


class RemixRouter:

    def db_for_read(self, model, **hints):

        if "remix" in model._meta.app_label:
            return "remix"
        return None

    def db_for_write(self, model, **hints):

        if "remix" in model._meta.app_label:
            return "remix"
        return None

    def allow_relation(self, obj1, obj2, **hints):

        if "remix" in obj1._meta.app_label or "remix" in obj2._meta.app_label:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):

        # if "remix" in app_label:
        #     return db == "remix"
        return False
