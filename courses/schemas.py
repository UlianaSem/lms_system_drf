from drf_yasg import openapi

request_body = openapi.Schema(
    title="Course",
    type=openapi.TYPE_OBJECT,
    properties={
        'name': openapi.Schema(type=openapi.TYPE_STRING, title="Name", minLength=1),
        'preview': openapi.Schema(type=openapi.TYPE_FILE, title="Изображение", nullable=True),
        'description': openapi.Schema(type=openapi.TYPE_STRING, title="Description", minLength=1, nullable=True),
        'price': openapi.Schema(type=openapi.TYPE_INTEGER, title="Price"),
        'students': openapi.Schema(type=openapi.TYPE_ARRAY, title="Students", items=openapi.Schema(
            type=openapi.TYPE_INTEGER), uniqueItems=True),
    }
)

responses = {200: openapi.Schema(
    title="Course",
    type=openapi.TYPE_OBJECT,
    properties={
        'name': openapi.Schema(type=openapi.TYPE_STRING, title="Name", minLength=1),
        'preview': openapi.Schema(type=openapi.TYPE_FILE, title="Изображение", nullable=True),
        'description': openapi.Schema(type=openapi.TYPE_STRING, title="Description", minLength=1, nullable=True),
        'lessons_count': openapi.Schema(type=openapi.TYPE_INTEGER, title="Lessons count", read_only=True),
        'subscription_sign': openapi.Schema(type=openapi.TYPE_BOOLEAN, title="Subscription sign", read_only=True),
    }
)
}
