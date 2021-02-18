from unittest import TestLoader, TestSuite
#from pyunitreport import HTMLTestRunner
from HtmlTestRunner import HTMLTestRunner
from assertions import AssertionsTest
from searchtest import SearchTests


assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_tests = TestLoader().loadTestsFromTestCase(SearchTests)

#contruimos la suite de pruebas
smoke_test = TestSuite([assertions_test, search_tests])


#para generar los reporters


#la variable runner almacena un reporte generado por HTMLTestRuner
#usa como argumento "kwarsp"
runner = HTMLTestRunner(combine_reports=True, report_name="Reporte-combinado")

#h = HtmlTestRunner.HTMLTestRunner(combine_reports=True).run(suite)

#corro el rurner con la suite de prueba
runner.run(smoke_test) 
#gracias