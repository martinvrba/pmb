import logging
import os
import pay_by_square
import qrcode
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, viewsets
from rest_framework.parsers import JSONParser
from .models import Payment
from .serializers import PaymentSerializer

logger = logging.getLogger(__name__)

# Create your views here.


# TODO: remove
@csrf_exempt
def generate_qr_code(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = PaymentSerializer(data=data)
        if serializer.is_valid():
            payment = serializer.save()
            OUTPUT_DIR = "pmb/static/pmb/qr-codes"
            OUTPUT_FORMAT = "png"
            os.system(f"mkdir -p {OUTPUT_DIR}")
            pbs_code = pay_by_square.generate(
                amount=payment.amount,
                beneficiary_address_1=payment.beneficiary_address1,
                beneficiary_address_2=payment.beneficiary_address2,
                beneficiary_name=payment.beneficiary_name,
                constant_symbol=payment.constant_symbol,
                currency="EUR",
                date=payment.due_date,
                iban=payment.iban,
                note=payment.payment_note,
                specific_symbol=payment.specific_symbol,
                swift="",
                variable_symbol=payment.variable_symbol,
            )
            pbs_img = qrcode.make(pbs_code)
            pbs_img.save(f"{OUTPUT_DIR}/{payment.id}.{OUTPUT_FORMAT}")
            logger.info(
                f"QR code generated in {OUTPUT_DIR}/{payment.id}.{OUTPUT_FORMAT}"
            )
            return JsonResponse({"filename": payment.id, "filename_ext": OUTPUT_FORMAT})
        else:
            logger.error(serializer.errors)
            return HttpResponse(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class PaymentView(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
