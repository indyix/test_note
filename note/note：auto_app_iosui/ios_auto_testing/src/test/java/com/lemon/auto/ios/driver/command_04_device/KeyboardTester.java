package com.lemon.auto.ios.driver.command_04_device;

import java.net.URL;
import java.util.Map;

import org.openqa.selenium.By;
import org.openqa.selenium.ScreenOrientation;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.testng.internal.Yaml;

import io.appium.java_client.ios.IOSDriver;
import io.appium.java_client.ios.IOSElement;

public class KeyboardTester {
	public static void main(String[] args) throws Exception {
		// 期望的能力对象
		DesiredCapabilities desiredCapabilities = new DesiredCapabilities();
		// 平台名
		desiredCapabilities.setCapability("platformName", "iOS");
		// 平台版本
		desiredCapabilities.setCapability("platformVersion", "13.1");
		// app文件的路径
		desiredCapabilities.setCapability("app", "/Users/nick/Desktop/tools/app/UICatalog.app");
		// 设备名
		desiredCapabilities.setCapability("deviceName", "iPhone 8");
		// 创建一个会话
		URL remoteAddress = new URL("http://localhost:4723/wd/hub");
		IOSDriver<IOSElement> driver = new IOSDriver<IOSElement>(remoteAddress, desiredCapabilities);

		// 软键盘是否显示
		System.out.println(driver.isKeyboardShown());
		

		driver.findElementByAccessibilityId("id_cell_text_fields").click();

		IOSElement element = driver.findElementByAccessibilityId("id_tv_default");
		element.click();
		element.sendKeys("123456");

		// 软键盘是否显示
		System.out.println(driver.isKeyboardShown());

		// 隐藏软键盘
		Thread.sleep(3000);
		driver.hideKeyboard();

		Thread.sleep(3000);
		driver.quit();

	}

}
