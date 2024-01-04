from rest_framework.throttling import UserRateThrottle,AnonRateThrottle
from django.core.cache import caches


class BurstRateThrottle(AnonRateThrottle):
    scope = "burst"

class SimpleRateThrottle(AnonRateThrottle):
    scope = "simple"