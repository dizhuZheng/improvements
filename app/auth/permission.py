from flask_principal import Permission, RoleNeed
from functools import wraps

NORMAL = "NORMAL"
ADMIN = "ADMIN"
ROLES = ("NORMAL","ADMIN")

admin_permission = Permission(RoleNeed('Admin'))

def admin_authority(func):
  @wraps
  def decorated_view(*args, **kwargs):
    if admin_permission.can():
      return func(*args, **kwargs)
    else:
      return "Not Admin User"
  return decorated_view
  
