# noqa: F401,W0611
# pylint: disable=unused-import

from .deploy.kanidm import on_create_kanidms, on_update_kanidms  # noqa
from .deploy.account import (
    on_create_account,
    on_update_account,
    on_delete_account,
)  # noqa
from .deploy.group import (
    on_create_group,
    on_update_group_name,
    on_update_group_members,
    on_delete_group,
)  # noqa

from .deploy.user import (
    on_create_user, 
    #on_update_user, 
    #on_delete_user  
) # noqa