from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Car
from .serializers import CarSerializer


class CarPublicViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarPrivateViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self):
        return Car.objects.filter(user=self.request.user)

    def create(self, serializer):
        # Get the user associated with the provided access token
        user = self.request.user

        company = self.request.data.get('company')
        model = self.request.data.get('model')
        number = self.request.data.get('number')
        image = self.request.data.get('image')
        details = self.request.data.get('details')

        # Create the Coupon object with the provided data
        coupon = Car(
            user=user,
            company=company,
            model=model,
            number=number,
            image=image,
            details=details
        )

        coupon.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)