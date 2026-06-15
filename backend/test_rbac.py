from backend.security.rbac import (
    require_role
)

require_role(
    "admin",
    ["admin", "operator"]
)

print("Access Granted")