from bottle import Bottle, request, response
import json
from random import randint
from datetime import datetime

assets_endpoint= "http://yoisho_soap"

wsdl='''<?xml version='1.0' encoding='UTF-8'?><wsdl:definitions xmlns:plink="http://schemas.xmlsoap.org/ws/2003/05/partner-link/" xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" xmlns:soap11enc="http://schemas.xmlsoap.org/soap/encoding/" xmlns:soap11env="http://schemas.xmlsoap.org/soap/envelope/" xmlns:soap12enc="http://www.w3.org/2003/05/soap-encoding" xmlns:soap12env="http://www.w3.org/2003/05/soap-envelope" xmlns:tns="yoisho.total.assets" xmlns:wsa="http://schemas.xmlsoap.org/ws/2003/03/addressing" xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/" xmlns:xop="http://www.w3.org/2004/08/xop/include" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" targetNamespace="yoisho.total.assets" name="Application"><wsdl:types><xs:schema targetNamespace="yoisho.total.assets" elementFormDefault="qualified"><xs:complexType name="stringArray"><xs:sequence><xs:element name="string" type="xs:string" minOccurs="0" maxOccurs="unbounded" nillable="true"/></xs:sequence></xs:complexType><xs:complexType name="bank_assets"/><xs:complexType name="bank_debt"/><xs:complexType name="bank_assetsResponse"><xs:sequence><xs:element name="bank_assetsResult" type="tns:stringArray" minOccurs="0" nillable="true"/></xs:sequence></xs:complexType><xs:complexType name="bank_debtResponse"><xs:sequence><xs:element name="bank_debtResult" type="tns:stringArray" minOccurs="0" nillable="true"/></xs:sequence></xs:complexType><xs:element name="stringArray" type="tns:stringArray"/><xs:element name="bank_assets" type="tns:bank_assets"/><xs:element name="bank_debt" type="tns:bank_debt"/><xs:element name="bank_assetsResponse" type="tns:bank_assetsResponse"/><xs:element name="bank_debtResponse" type="tns:bank_debtResponse"/></xs:schema></wsdl:types><wsdl:message name="bank_debt"><wsdl:part name="bank_debt" element="tns:bank_debt"/></wsdl:message><wsdl:message name="bank_debtResponse"><wsdl:part name="bank_debtResponse" element="tns:bank_debtResponse"/></wsdl:message><wsdl:message name="bank_assets"><wsdl:part name="bank_assets" element="tns:bank_assets"/></wsdl:message><wsdl:message name="bank_assetsResponse"><wsdl:part name="bank_assetsResponse" element="tns:bank_assetsResponse"/></wsdl:message><wsdl:service name="TotalAssetsService"><wsdl:port name="Application" binding="tns:Application"><soap:address location="''' + assets_endpoint + '''"/></wsdl:port></wsdl:service><wsdl:portType name="Application"><wsdl:operation name="bank_debt" parameterOrder="bank_debt"><wsdl:input name="bank_debt" message="tns:bank_debt"/><wsdl:output name="bank_debtResponse" message="tns:bank_debtResponse"/></wsdl:operation><wsdl:operation name="bank_assets" parameterOrder="bank_assets"><wsdl:input name="bank_assets" message="tns:bank_assets"/><wsdl:output name="bank_assetsResponse" message="tns:bank_assetsResponse"/></wsdl:operation></wsdl:portType><wsdl:binding name="Application" type="tns:Application"><soap:binding style="document" transport="http://schemas.xmlsoap.org/soap/http"/><wsdl:operation name="bank_debt"><soap:operation soapAction="bank_debt" style="document"/><wsdl:input name="bank_debt"><soap:body use="literal"/></wsdl:input><wsdl:output name="bank_debtResponse"><soap:body use="literal"/></wsdl:output></wsdl:operation><wsdl:operation name="bank_assets"><soap:operation soapAction="bank_assets" style="document"/><wsdl:input name="bank_assets"><soap:body use="literal"/></wsdl:input><wsdl:output name="bank_assetsResponse"><soap:body use="literal"/></wsdl:output></wsdl:operation></wsdl:binding></wsdl:definitions>'''

app = Bottle()

@app.route("/", method='GET')
@app.route("/soap", method='GET')
def get_wsdl():
    response.content_type = 'text/xml; charset=utf-8'
    return wsdl

@app.route("/", method='POST')
@app.route('/soap', method='POST')
def do_soap():


    assets_response = '''<soap11env:Envelope xmlns:soap11env="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tns="yoisho.total.assets">
   <soap11env:Body>
      <tns:bank_assetsResponse>
         <tns:bank_assetsResult>
            <tns:string>''' + str(randint(9900000,9999999))+ '''</tns:string>
         </tns:bank_assetsResult>
      </tns:bank_assetsResponse>
   </soap11env:Body>
</soap11env:Envelope>'''

    debt_response = '''<soap11env:Envelope xmlns:soap11env="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tns="yoisho.total.assets">
       <soap11env:Body>
          <tns:bank_debtResponse>
             <tns:bank_debtResult>
                <tns:string>''' + str(randint(1000000,1999999))+ '''</tns:string>
             </tns:bank_debtResult>
          </tns:bank_debtResponse>
       </soap11env:Body>
    </soap11env:Envelope>'''

    action = str(request.headers.get('SOAPAction'))

    response.content_type = 'text/xml; charset=utf-8'
    if "bank_assets" in action:
        return assets_response
    else:
        return debt_response
