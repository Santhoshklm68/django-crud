from rest_framework.routers import DefaultRouter
from app.views import StudentViewsets

router  = DefaultRouter()

router.register("student", StudentViewsets)