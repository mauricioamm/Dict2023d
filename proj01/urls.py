
from django.contrib import admin
from django.urls import path, include
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from dictapp import views
from dictapp.views import editar_ale, editar_ing, \
                            sessao_testar_ale, sessao_testar_ing,\
                            principal_ale, principal_ing,\
                            Entrada_Iniciar, Entrada_login,\
                            Entrada_sobre, Entrada,\
                            Entrada_configuracoes, Entrada_relatorios,\
                            sessao_testar_audio_ale, sessao_testar_port_ale, sessao_testar_figura_ale,\
                            sessao_testar_audio_ing, sessao_testar_port_ing, sessao_testar_figura_ing,\
                            sessao_upload_ale, sessao_upload_ing,\
                            sessao_tabela_ale, sessao_tabela_ing, parabens_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Entrada, name='url_entrada'),
    #path('', views.Home.as_view(), name='home'),
    # path('upload', views.upload, name='upload'),

    path('Entrada_Iniciar/', Entrada_Iniciar, name='url_Entrada_Iniciar'),
    path('Entrada_login/', Entrada_login, name='url_Entrada_login'),
    path('Entrada_configuracoes/', Entrada_configuracoes, name='url_Entrada_configuracoes'),
    path('Entrada_relatorios/', Entrada_relatorios, name='url_Entrada_relatorios'),
    path('Entrada_sobre/', Entrada_sobre, name='url_Entrada_sobre'),

    path('editar_ale/<int:pk>/', editar_ale, name='url_editar_ale'),

    path('editar_ing/<int:pk>/', editar_ing, name='url_editar_ing'),

    path('principal_ale/<int:pk>/', principal_ale, name='url_principal_ale'),
    path('principal_ing/<int:pk>/', principal_ing, name='url_principal_ing'),

    path('sessao_testar_ale/<int:pk>/', sessao_testar_ale, name='url_sessao_testar_ale'),
    path('sessao_testar_port_ale/<int:pk>/', sessao_testar_port_ale, name='url_sessao_testar_port_ale'),
    path('sessao_testar_audio_ale/<int:pk>/', sessao_testar_audio_ale, name='url_sessao_testar_audio_ale'),
    path('sessao_testar_figura_ale/<int:pk>/', sessao_testar_figura_ale, name='url_sessao_testar_figura_ale'),

    path('sessao_testar_ing/<int:pk>/', sessao_testar_ing, name='url_sessao_testar_ing'),
    path('sessao_testar_port_ing/<int:pk>/', sessao_testar_port_ing, name='url_sessao_testar_port_ing'),
    path('sessao_testar_audio_ing/<int:pk>/', sessao_testar_audio_ing, name='url_sessao_testar_audio_ing'),
    path('sessao_testar_figura_ing/<int:pk>/', sessao_testar_figura_ing, name='url_sessao_testar_figura_ing'),
    path('sessao_tabela_ale/<int:pk>/', sessao_tabela_ale, name='url_sessao_tabela_ale'),
    path('sessao_tabela_ing/<int:pk>/', sessao_tabela_ing, name='url_sessao_tabela_ing'),

    path('sessao_upload/<int:pk>/', sessao_upload_ing, name='url_sessao_upload_ing'),
    path('Parabens/', parabens_view, name='url_parabens_view'),
]
### chamar depois ###
if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)