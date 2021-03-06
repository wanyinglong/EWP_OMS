#encoding:utf-8
from django.conf.urls import url
from views import *
from file_local import *
from file_remote import *
from django.conf import settings

urlpatterns = [
    url(r'^target/$', target, name='target'),
    url(r'^command/$', command, name='command'),
    url(r'^server/$', server, name='server'),
    url(r'^minions/(?P<server_id>[0-9]+)/$', minions, name='minions'),
    url(r'^minions_fun/$', minions_fun, name='minions_fun'),
    url(r'^execute/$', execute, name='execute'),
    url(r'^result/$', result, name='result'),
    # url(r'^cmd_result_detail/(?P<result_id>[0-9]+)/$', cmd_result_detail, name='cmd_result_detail'),
    url(r'^jid_info/$', jid_info, name='jid_info'),
    url(r'^config/(?P<server_id>[0-9]+)/$', config, name='config'),
    url(r'^file_local/$', file_local, name='file_local'),
    url(r'^file_create/$', file_create, name='file_create'),
    url(r'^file_rename/$', file_rename, name='file_rename'),
    url(r'^file_write/$', file_write, name='file_write'),
    url(r'^file_delete/$', file_delete, name='file_delete'),
    url(r'^file_upload/$', file_upload, name='file_upload'),
    url(r'^svn/$', svn, name='svn'),
    url(r'^file_remote/(?P<server_id>[0-9]+)/$', file_remote, name='file_remote'),
    url(r'^file_remote_create/$', file_remote_create, name='file_remote_create'),
    url(r'^file_remote_rename/$', file_remote_rename, name='file_remote_rename'),
    url(r'^file_remote_write/$', file_remote_write, name='file_remote_write'),
    url(r'^file_remote_delete/$', file_remote_delete, name='file_remote_delete'),
    url(r'^deploy/(?P<server_id>[0-9]+)/$', deploy, name='deploy'),
    url(r'^deploy_fun/(?P<server_id>[0-9]+)/$', deploy_fun, name='deploy_fun'),


    # url(r'^file_download/(?P<file_name>.*)/$', file_download, name='file_download'),
    # url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    ]