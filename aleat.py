#!/usr/bin/python
import webapp
import random

  class aleat(webapp.webApp):

      def process(self, parsedRequest):
        """Parse"""
        num_al = random.randrange(100000)
        return ("200 OK", "<html><body><h1>Hello World!</h1>" +
                    "<a href='" + str(num_al) + "'>Dame otra url</a>" +
                    "</body></html>")

if __name__ == "__main__":
    testWebApp = aleat("localhost", 1234)

