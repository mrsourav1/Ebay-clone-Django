from . import views
from django.urls import path,include

urlpatterns = [

    path("",views.index,name = "index"),
    path("register",views.register,name = "register"),
    path("login",views.login_view,name = "login"),
    path("logout",views.logout_view,name ="logout"),
    path("create_listing",views.create_listing,name = "create_listing"),
    path("listings",views.listings,name = "listings"),
    path("listings/<int:listing_id>",views.listing_details,name = "listing_details"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("my_listings", views.my_listings, name="my_listings"),
]