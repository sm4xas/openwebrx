from owrx.command import Flag
from .soapy import SoapyConnectorSource


class AirspySource(SoapyConnectorSource):
    def getCommandMapper(self):
        return super().getCommandMapper().setMappings({"bias_tee": Flag("-t biastee=true")})

    def getDriver(self):
        return "airspy"

    def getEventNames(self):
        return super().getEventNames() + ["bias_tee"]
