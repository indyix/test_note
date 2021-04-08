package com.lemon.auto.ios.web;

import java.net.URL;
import java.time.Duration;
import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.Dimension;
import org.openqa.selenium.Point;
import org.openqa.selenium.Rectangle;
import org.openqa.selenium.ScreenOrientation;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.testng.internal.Yaml;

import io.appium.java_client.appmanagement.ApplicationState;
import io.appium.java_client.ios.IOSDriver;
import io.appium.java_client.ios.IOSElement;
import io.appium.java_client.remote.MobileCapabilityType;

public class WebTester {
	public static void main(String[] args) throws Exception {
		// 期望的能力对象
		DesiredCapabilities desiredCapabilities = new DesiredCapabilities();
		// 平台名
		desiredCapabilities.setCapability(MobileCapabilityType.PLATFORM_NAME, "iOS");
		// 平台版本
		desiredCapabilities.setCapability(MobileCapabilityType.PLATFORM_VERSION, "12.1");
		// 设置浏览器
		desiredCapabilities.setCapability(MobileCapabilityType.BROWSER_NAME, "Safari");
		// 设备名
		desiredCapabilities.setCapability(MobileCapabilityType.DEVICE_NAME, "iPhone 8");
		
		// 创建一个会话
		URL remoteAddress = new URL("http://localhost:4723/wd/hub");
		IOSDriver<IOSElement> driver = new IOSDriver<IOSElement>(remoteAddress, desiredCapabilities);

		driver.get("http://www.baidu.com");
		
//		driver.findElement(By.name("word")).sendKeys("软件测试");
		driver.findElement(By.id("index-kw")).sendKeys("测试");

//		Thread.sleep(3000);
//		driver.quit();

	}

}
