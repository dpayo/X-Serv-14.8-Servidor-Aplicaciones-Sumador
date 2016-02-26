import webapp

class sumapp(webapp.webApp):

    pnum=None
    def parse(self,request):
        num=request.split()[1][-1:]
        return num

    def process(self,parsedRequest):

        if(self.pnum ==None):
            self.pnum=parsedRequest;
            return("200 OK","<html><body><h1> Primer sumando "+self.pnum+" </h1></body></html>")
        else:
            num= parsedRequest
            try:
                suma = int(self.pnum) + int(num)
            except ValueError:
                self.pnum=None;
                return("400 Bad Request ","<html><body><h1> Error number not valid...</h1></body></html>")

            self.pnum=None;
            return("200 OK","<html><body><h1> Suma: "+str(suma)+"</h1></body></html>")

if __name__ == "__main__":

    sumador= sumapp("localhost",8000)
