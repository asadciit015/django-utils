from django_utils.management import commands


def test_settings_command_empty():
    command = commands.settings.Command()
    command.handle()


def test_settings_command_arg():
    command = commands.settings.Command()
    command.handle('debug')


def test_admin_autogen_command():
    command = commands.admin_autogen.Command()
    command.handle()
