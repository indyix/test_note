package com.lemon.auto.ios.driver.command_03_session;

import java.net.URL;
//import java.util.Map;
//
//import io.appium.java_client.android.AndroidDriver;
//import io.appium.java_client.android.AndroidElement;
import org.openqa.selenium.remote.DesiredCapabilities;

import io.appium.java_client.ios.IOSDriver;
import io.appium.java_client.ios.IOSElement;



public class SessionTester {
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
		// 1:创建会话
		IOSDriver<IOSElement> driver = new IOSDriver<IOSElement>(remoteAddress, desiredCapabilities);

		// 2:获取会话的id
//		SessionId sessionId = driver.getSessionId();
//		System.out.println(sessionId);
				// 3:结束会话
//		driver.quit();

				// 4:获取源代码（获取网页源码：程序层次结构XML (app)或页面源码(web)）
//		String pageSource = driver.getPageSource();
//		System.out.println(pageSource);

//		//5:返回（只适合web上下文）
//		AndroidDriver<AndroidElement> aDriver = null;
//		aDriver.navigate().back();


				Thread.sleep(3000);
		driver.quit();

	}

}
