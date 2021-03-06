from alembic import context


class AlembicEnv(object):

    def __init__(self, app, base_model, dbname):
        self.app = app
        self.base_model = base_model
        self.metadata = self.base_model.metadata
        self.dbname = dbname
        self.db = None

    def run(self):
        self._init_app()
        self.db = self.app.dbs[self.dbname]
        self._run_migration_depending_on_offline_mode()

    def _init_app(self):
        if context.config.get_main_option('is_test', False):
            self.app.run_tests()
        else:
            self.app.run_command()

    def _run_migration_depending_on_offline_mode(self):
        if context.is_offline_mode():
            self.run_migrations_offline()
        else:
            self.run_migrations_online()

    def run_migrations_offline(self):
        """Run migrations in 'offline' mode.

        This configures the context with just a URL
        and not an Engine, though an Engine is acceptable
        here as well.  By skipping the Engine creation
        we don't even need a DBAPI to be available.

        Calls to context.execute() here emit the given string to the
        script output.

        """
        url = self.db.get_url()

        context.configure(
            url=url,
            target_metadata=self.metadata,
            literal_binds=True)

        self.run_migrations()

    def run_migrations_online(self):
        """Run migrations in 'online' mode.

        In this scenario we need to create an Engine
        and associate a connection with the context.

        """
        connectable = self.db.get_engine()

        with connectable.connect() as connection:
            context.configure(
                connection=connection,
                target_metadata=self.metadata)

            self.run_migrations()

    def run_migrations(self):
        with context.begin_transaction():
            context.run_migrations()
