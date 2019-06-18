from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

if __name__ == "__main__":

  # ヘッドレスにするためのオプション
  options = webdriver.ChromeOptions()
  options.add_argument('--headless')
  driver = webdriver.Chrome(options=options)

  # page にアクセス
  driver.get('http://www.customs.go.jp/toukei/srch/index.htm?M=77&P=1,1,,,,1,,,,2,,2016,2019,,,7,853224000,,,,,,,,,,1,,,,,,,,,,,1,,,,,,,,,,,')
  print(driver.title)

  # frame を切り替える
  driver.switch_to_frame("FR_M_INFO")

  # page　のソースを表示する
  # ソースの中に数値データは入っている
  print(driver.page_source)


  # ここがうまくいかない。選択できていない?
  tableElem = driver.find_elements_by_id("h2")
  # trs = tableElem.find_element_by_class_name("table")

  print(tableElem)

  # driver.save_screenshot('seamrch_results.png')
  driver.quit()