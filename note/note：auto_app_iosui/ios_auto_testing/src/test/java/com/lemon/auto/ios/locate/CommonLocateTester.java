package com.lemon.auto.ios.locate;

import java.net.URL;
import java.util.List;

import org.openqa.selenium.By;
import org.openqa.selenium.remote.DesiredCapabilities;

import io.appium.java_client.ios.IOSDriver;
import io.appium.java_client.ios.IOSElement;


public class CommonLocateTester {
	public static void main(String[] args) throws Exception {
		//期望的能力对象
		DesiredCapabilities desiredCapabilities = new DesiredCapabilities();
		desiredCapabilities.setCapability("platformName", "iOS");//平台名
		desiredCapabilities.setCapability("platformVersion", "13.1");//平台版本
		desiredCapabilities.setCapability("app", "/Users/nick/Desktop/tools/app/UICatalog.app");//app文件的路径
		desiredCapabilities.setCapability("deviceName", "iPhone 8");//设备名

		URL remoteAddress = new URL("http://localhost:4723/wd/hub");
		IOSDriver<IOSElement> driver = new IOSDriver<IOSElement>(remoteAddress, desiredCapabilities);
		
		//1:id，iOS的元素是没有这个属性的，但是我们用name属性作为id使用
//		IOSElement element = driver.findElement(By.id("id_cell_action_sheet"));
//		element.click();
		
		//2:name:一般和accessibility id值相同
//		IOSElement element = driver.findElementByName("id_cell_action_sheet");
//		element.click();
		
		//3:className: 检查器中的type属性值
//		List<IOSElement> elements = driver.findElements(By.className("XCUIElementTypeCell"));
//		System.out.println(elements.size());
//		elements.get(1).click();
		
		//4:xpath: appium对xpath的解析速度较慢
		driver.findElement(By.xpath("//XCUIElementTypeCell[@name=\"id_cell_alert\"]")).click();
		
//		Thread.sleep(3000);
//		driver.quit();

		
	}

}
