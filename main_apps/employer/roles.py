from rolepermissions.roles import AbstractUserRole

class Employer(AbstractUserRole):
    available_permissions = {
        'access_dash_employer': True,
        # ... autres permissions nécessaires ...
    }
