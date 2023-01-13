import unittest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from time import sleep

class AppiumTest(unittest.TestCase):
	def test_0(self): # En este test probamos a abrir la app Calculadora
		# Configuramos el driver
		driver = {
			"platformName": "Android",
			"appium:platformVersion": "12",
			"appium:deviceName": "OnePlus7T",
			"appium:automationName": "UiAutomator2",
			"appium:appPackage": "com.oneplus.calculator",
			"appium:appActivity": "com.oneplus.calculator.Calculator"
			}

		# Conectamos con Appium
		driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', driver) # La dirección es la del servidor de Appium que es quien se pone en contacto con el movil

		# Cerramos la App
		driver.close_app()

	def test_1(self): # En este test probamos a hacer una suma en la calculadora
		# Configuramos el driver
		driver = {
			"platformName": "Android",
			"appium:platformVersion": "12",
			"appium:deviceName": "OnePlus7T",
			"appium:automationName": "UiAutomator2",
			"appium:appPackage": "com.oneplus.calculator",
			"appium:appActivity": "com.oneplus.calculator.Calculator"
			}

		# Conectamos con Appium
		driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', driver) # La dirección es la del servidor de Appium que es quien se pone en contacto con el movil

		# Suma de dos números
		driver.find_element(MobileBy.ID, "com.oneplus.calculator:id/digit_7").click()
		driver.find_element(MobileBy.ID , "com.oneplus.calculator:id/op_add").click()
		driver.find_element(MobileBy.ID , "com.oneplus.calculator:id/digit_7").click()
		driver.find_element(MobileBy.ID , "com.oneplus.calculator:id/eq").click()
		sleep(3)

		# Limpiamos resultado
		driver.find_element(MobileBy.ID, "com.oneplus.calculator:id/clr").click()
		sleep(3)

		# Cerramos la App
		driver.close_app()

	def test_2(self):
		# Configuramos el driver
		driver = {
			"platformName": "Android",
			"appium:platformVersion": "12",
			"appium:deviceName": "OnePlus7T",
			"appium:automationName": "UiAutomator2",
			"appium:appPackage": "com.android.vending",
			"appium:appActivity": "com.android.vending.AssetBrowserActivity"
			}

		# Conectamos con Appium
		driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', driver)

		# Hacemos click en la barra de búsqueda
		driver.find_element(MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ImageView[1]").click()

		# Escondemos el teclado ya que no lo necesitamos
		driver.hide_keyboard()

		# Introducimos texto en la barra de búsqueda
		driver.find_element(MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.EditText").send_keys("infojobs")

		# Hacemos click en la primera opción
		driver.find_element(MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]").click()
		sleep(1)

		# Hacemos click en la app a descargar, en este caso infojobs
		driver.find_element(MobileBy.XPATH, '//android.widget.FrameLayout[@content-desc="InfoJobs - Trabajo y Empleo, Adevinta Spain, S.L.U., Contiene anuncios"]').click()
		sleep(1)

		# Hacemos click en descargar (suponiendo que no está instalada)
		driver.find_element(MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.Button").click()
		sleep(30)

		# Hacemos click en abrir para demostrar que se ha descargado
		driver.find_element(MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.Button[2]").click()
		sleep(10)

		# Cerramos la App
		driver.close_app()


if __name__ == '__main__':
	unittest.main()
