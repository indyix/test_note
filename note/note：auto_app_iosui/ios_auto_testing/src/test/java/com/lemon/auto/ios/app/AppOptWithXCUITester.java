package com.lemon.auto.ios.app;

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

public class AppOptWithXCUITester {
	/**
	 * mac osx：10.14 appium：v.12.1 xcode：10.1 iOS:12.1
	 * 
	 * @param args
	 * @throws Exception
	 */
	public static void main(String[] args) throws Exception {
		// 期望的能力对象
		DesiredCapabilities desiredCapabilities = new DesiredCapabilities();
		// 平台名
		desiredCapabilities.setCapability("platformName", "iOS");
		// 平台版本
		desiredCapabilities.setCapability("platformVersion", "12.1");
		// app文件的路径
		desiredCapabilities.setCapability("app", "/Users/happy/Desktop/tools/app/UICatalog.app");
		// 设备名
		desiredCapabilities.setCapability("deviceName", "iPhone 8");
		// 是否重置app设置
		desiredCapabilities.setCapability("noReset", true);
		// 创建一个会话
		URL remoteAddress = new URL("http://localhost:4723/wd/hub");
		IOSDriver<IOSElement> driver = new IOSDriver<IOSElement>(remoteAddress, desiredCapabilities);
		String bundleId = "com.example.apple-samplecode.UICatalog";
		
//		安装应用
		Thread.sleep(3000);
		Map<String, Object> params = new HashMap<String, Object>()	;
		params.put("app", "/Users/happy/Desktop/tools/app/UICatalog.app");
		driver.executeScript("mobile: installApp",params);
//		app: .ipa的完整路径
//		无
//		查看应用是否安装
//		driver.executeScript("mobile:isAppInstalled",params);
//		bundleId
//		true表示已安装
//		启动应用
//		driver.executeScript("mobile:launchApp",params);
//		bundleId
//		无
//		移除应用
//		Thread.sleep(3000);
//		Map<String, Object> params = new HashMap<String, Object>();
//		params.put("bundleId", bundleId);
//		driver.executeScript("mobile: removeApp",params);
//		bundleId
//		true表示移除成功
//		激活应用
//		driver.executeScript("mobile:activateApp",params);
//		bundleId
//		无
//		退出应用
//		driver.executeScript("mobile:terminateApp",params);
//		bundleId
//		正在运行的App成功退出返回true
//		查看应用状态
//		driver.executeScript("mobile:queryAppState",params);
//		bundleId
//		0:当前应用程序状态无法确定或未知
//		1:应用程序没有运行
//		2:应用程序在后台运行并被挂起
//		3:应用程序在后台运行，没有挂起
//		4:应用程序在前台运行


//		Thread.sleep(3000);
//		driver.quit();

	}

}
