package com.lemon.auto.ios.locate;

import java.net.URL;
import java.util.List;

import org.openqa.selenium.By;
import org.openqa.selenium.remote.DesiredCapabilities;

import io.appium.java_client.MobileBy;
import io.appium.java_client.ios.IOSDriver;
import io.appium.java_client.ios.IOSElement;

public class MobileByLocateTester {
	public static void main(String[] args) throws Exception {
		// 期望的能力对象
		DesiredCapabilities desiredCapabilities = new DesiredCapabilities();
		desiredCapabilities.setCapability("platformName", "iOS");// 平台名
		desiredCapabilities.setCapability("platformVersion", "13.1");// 平台版本
		desiredCapabilities.setCapability("app", "/Users/nick/Desktop/tools/app/UICatalog.app");// app文件的路径
		desiredCapabilities.setCapability("deviceName", "iPhone 8");// 设备名

		URL remoteAddress = new URL("http://localhost:4723/wd/hub");
		IOSDriver<IOSElement> driver = new IOSDriver<IOSElement>(remoteAddress, desiredCapabilities);

		// 1:替代以前的name定位方式，推荐使用
		// ios：name值
		// Android：content-desc
//		driver.findElementByAccessibilityId("id_cell_action_sheet").click();
//		driver.findElement(MobileBy.AccessibilityId("id_cell_indicators")).click();

		// 2:IosClassChain 类型链
//		仅限在 WebDriverAgent 框架使用(ios10)，用于替代 xpath
//		比较灵活，但是待完善
//		如找到第一个cell
//		String classChain = "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[3]";
//		String classChain = "XCUIElementTypeWindow[1]/*/*/*/*/XCUIElementTypeCell[4]";
		String classChain = "*/*/*/*/*/XCUIElementTypeCell[4]";
//		driver.findElementByIosClassChain(classChain).click();
//		driver.findElement(MobileBy.iOSClassChain(classChain)).click();

		Thread.sleep(3000);
		driver.quit();


	}

}
