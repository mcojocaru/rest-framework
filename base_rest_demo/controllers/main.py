# -*- coding: utf-8 -*-
# Copyright 2018 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.addons.base_rest.controllers import main


class BaseRestDemoPublicApiController(main.RestController):
    _root_path = '/base_rest_demo_api/public/'
    _collection_name = 'base.rest.demo.public.services'
    _default_auth = 'public'


class BaseRestDemoPrivateApiController(main.RestController):
    _root_path = '/base_rest_demo_api/private/'
    _collection_name = 'base.rest.demo.private.services'
    _default_auth = 'user'
