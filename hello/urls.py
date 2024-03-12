
from hello import views
from django.urls import path


urlpatterns = [
    path("",views.home,name="homepage"), 
    path("about/",views.about,name="About"),
    path("contact/",views.contactx,name="ContactUs"),
    path("service/",views.servicex,name="services"),
    path("navbar/",views.nav,name="navabr"),
    path("save-my-data",views.savethis),
    path("deleterecord/<int:myid>",views.deletedata),
    path("updaterecord/<int:myid>",views.updatethisdataok),
    path("updatedata/<int:update>",views.updatenow),
    path("search",views.searchthisdata, name="mysearch"),
    path("signup_page",views.signpage,name="signup"),
    path("signup",views.signup,),
    path("login",views.logins,name="login"),
    path("loginup",views.loginup),
    path("logoutthis",views.logouthere,name="logout")
    


]
