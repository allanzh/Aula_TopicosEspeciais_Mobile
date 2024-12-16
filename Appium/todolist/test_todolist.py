from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
import unittest
import time


class TestAppToDoMethods(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		options = AppiumOptions()
		options.load_capabilities({
			"platformName": "Android",
			"appium:automationName": "uiautomator2",
		})

		cls.driver = webdriver.Remote("http://192.168.1.3:4723", options=options)
		cls.packageName = 'com.enoiu.todo'
		cls.driver.activate_app(cls.packageName)
		#time.sleep(2)

		return super().setUpClass()
	
	def setUp(self):
		# Limpar os dados do app antes de executar os testes
		btn_tab_settings = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Settings\nTab 4 of 4')
		btn_tab_settings.click()

		uiSelector = "new UiSelector().description(\"Delete Data\").instance(1)"
		command = "new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(" + uiSelector + ");"

		btn_delete_data = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=command)
		btn_delete_data.click()

		btn_confirm_delete_data = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="Delete"]')
		btn_confirm_delete_data.click()

		# Voltar pra aba principal do app
		btn_tab_ToDo = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='ToDo\nTab 1 of 4')
		btn_tab_ToDo.click()		

		return super().setUp()
	
	def test_addTask(self):
		
		# Click no botão de new task
		btn_new_task = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.Button\").instance(1)")
		btn_new_task.click()
	
		tituloTarefa = "Tarefa Teste"
	
		#Preencher titulo da task
		txt_title_task = self.driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")
		txt_title_task.send_keys(tituloTarefa)
	
		# Click no botão de add task
		btn_add_task = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Add")
		btn_add_task.click()

		# Assert task cadastrada
		txt_title_task_created = self.driver.find_elements(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="' + tituloTarefa + '"]')
		assert(len(txt_title_task_created) == 1)
	
	def test_deleteTask(self):

		# Click no botão de new task
		btn_new_task = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.Button\").instance(1)")
		btn_new_task.click()
	
		tituloTarefa = "Tarefa Teste 2"
	
		#Preencher titulo da task
		txt_title_task = self.driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")
		txt_title_task.send_keys(tituloTarefa)
	
		# Click no botão de add task
		btn_add_task = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Add")
		btn_add_task.click()
	
		# Assert task cadastrada
		txt_title_task_created = self.driver.find_elements(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="' + tituloTarefa + '"]')
		assert(len(txt_title_task_created) == 1)

		# Click no botão de opções da task
		btn_func_tasks = self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="' + tituloTarefa + '"]/android.widget.Button')
		btn_func_tasks.click()

		# Click no botão de delete task
		btn_delete_task = self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="Delete"]')
		btn_delete_task.click()

		# Assert task deletada
		txt_title_task_created = self.driver.find_elements(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="' + tituloTarefa + '"]')
		assert(len(txt_title_task_created) == 0)

	def test_editTask(self):

		# Click no botão de new task
		btn_new_task = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.Button\").instance(1)")
		btn_new_task.click()
	
		tituloTarefa = "Tarefa Teste 3"
	
		#Preencher titulo da task
		txt_title_task = self.driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")
		txt_title_task.send_keys(tituloTarefa)
	
		# Click no botão de add task
		btn_add_task = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Add")
		btn_add_task.click()
	
		# Assert task cadastrada
		txt_title_task_created = self.driver.find_elements(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="' + tituloTarefa + '"]')
		assert(len(txt_title_task_created) == 1)

		# Click no botão de opções da task
		btn_func_tasks = self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="' + tituloTarefa + '"]/android.widget.Button')
		btn_func_tasks.click()

		# Click no botão de edit task
		btn_edit_task = self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="Edit"]')
		btn_edit_task.click()

		#Preencher titulo da task
		tituloTarefa = "Tarefa Teste 3 - Editada"
		txt_title_task = self.driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")
		txt_title_task.clear()
		txt_title_task.send_keys(tituloTarefa)

		# Click no botão de edit task
		btn_add_task = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Edit")
		btn_add_task.click()

		# Assert task editada
		txt_title_task_created = self.driver.find_elements(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="' + tituloTarefa + '"]')
		assert(len(txt_title_task_created) == 1)

	def test_markTaskAsDone(self):

		# Click no botão de new task
		btn_new_task = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.Button\").instance(1)")
		btn_new_task.click()
	
		tituloTarefa = "Tarefa Teste Concluida"
	
		#Preencher titulo da task
		txt_title_task = self.driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")
		txt_title_task.send_keys(tituloTarefa)
	
		# Click no botão de add task
		btn_add_task = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Add")
		btn_add_task.click()
	
		# Assert task cadastrada
		txt_title_task_created = self.driver.find_elements(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="' + tituloTarefa + '"]')
		assert(len(txt_title_task_created) == 1)

		# CLick no botão de check task
		btn_check_first_task = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().className("android.widget.CheckBox").instance(0)')
		btn_check_first_task.click()

		# CLick no botão da aba Done
		btn_tab_done = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Done\nTab 2 of 4')
		btn_tab_done.click()

		# Assert task done
		txt_title_task_created = self.driver.find_elements(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="' + tituloTarefa + '"]')
		assert(len(txt_title_task_created) == 1)

	def test_markAllTasksAsDone(self):
	
		# Click no botão de new task
		btn_new_task = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.Button\").instance(1)")

		tituloTarefaInicio = "Tarefa Teste Concluida - "

		for iteracao in range(3):
			btn_new_task.click()
			tituloTarefaAtual = tituloTarefaInicio + str(iteracao + 1)

			#Preencher titulo da task
			txt_title_task = self.driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")
			txt_title_task.send_keys(tituloTarefaAtual)
		
			# Click no botão de add task
			btn_add_task = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Add")
			btn_add_task.click()
		
			# Assert task cadastrada
			txt_title_task_created = self.driver.find_elements(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="' + tituloTarefaAtual + '"]')
			assert(len(txt_title_task_created) == 1)

			# CLick no botão de check task
			btn_check_first_task = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().className("android.widget.CheckBox").instance(0)')
			btn_check_first_task.click()

		# CLick no botão da aba Done
		btn_tab_done = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Done\nTab 2 of 4')
		btn_tab_done.click()

		for iteracao in range(3):
			tituloTarefaAtual = tituloTarefaInicio + str(iteracao + 1)

			# Assert task done
			txt_title_task_created = self.driver.find_elements(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="' + tituloTarefaAtual + '"]')
			assert(len(txt_title_task_created) == 1)

	def test_deleteAllTasksDone(self):
	
		# Click no botão de new task
		btn_new_task = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.Button\").instance(1)")

		tituloTarefaInicio = "Tarefa Teste Concluida - "

		for iteracao in range(3):
			btn_new_task.click()
			tituloTarefaAtual = tituloTarefaInicio + str(iteracao + 1)

			#Preencher titulo da task
			txt_title_task = self.driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")
			txt_title_task.send_keys(tituloTarefaAtual)
		
			# Click no botão de add task
			btn_add_task = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Add")
			btn_add_task.click()
		
			# Assert task cadastrada
			txt_title_task_created = self.driver.find_elements(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="' + tituloTarefaAtual + '"]')
			assert(len(txt_title_task_created) == 1)

			# CLick no botão de check task
			btn_check_first_task = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().className("android.widget.CheckBox").instance(0)')
			btn_check_first_task.click()

		# CLick no botão da aba Done
		btn_tab_done = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Done\nTab 2 of 4')
		btn_tab_done.click()

		for iteracao in range(3):
			tituloTarefaAtual = tituloTarefaInicio + str(iteracao + 1)

			# Assert task done
			txt_title_task_created = self.driver.find_elements(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="' + tituloTarefaAtual + '"]')
			assert(len(txt_title_task_created) == 1)

		btn_delete_all_tasks = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().className("android.widget.Button").instance(1)')
		btn_delete_all_tasks.click()

		btn_confirm_delete_all_tasks = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="Delete"]')
		btn_confirm_delete_all_tasks.click()

		txt_title_task_created = self.driver.find_elements(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="Tarefa Teste Concluida - 1"]')
		assert(len(txt_title_task_created) == 0)

	@classmethod
	def tearDownClass(cls):
		cls.driver.terminate_app(cls.packageName)
		cls.driver.quit()
		return super().tearDownClass()

if __name__ == '__main__':
    unittest.main()
