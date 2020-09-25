# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from django.conf.urls import url

from tecken.base import admin


app_name = "siteadmin"
urlpatterns = [
    url("^sitestatus/$", admin.site_status, name="site_status"),
]
