from commands.base import base_router
from commands.register import register_router
from commands.admin import admin_router
from commands.admin_spec import spec_router
from commands.admin_subj import subj_router
from commands.schedule import schedule_router

all_routers = [base_router, register_router, admin_router, spec_router, subj_router, schedule_router]
