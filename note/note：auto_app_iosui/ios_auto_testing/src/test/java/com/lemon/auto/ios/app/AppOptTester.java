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
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.testng.internal.Yaml;

import io.appium.java_client.appmanagement.ApplicationState;
import io.appium.java_client.ios.IOSDriver;
import io.appium.java_client.ios.IOSElement;

public class AppOptTester {
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
//		1:安装应用
//		Thread.sleep(2000);
//		driver.installApp("/Users/happy/Desktop/tools/app/UICatalog.app");
//		App的完整路径
//		无

//		2:查看应用是否安装:bundleId:相当于安卓app的包名，找开发人员要--》
//		boolean flag = driver.isAppInstalled(bundleId);
//		System.out.println(flag);
//		App的bundleId
//		true表示已安装，false表示未安装
		
//		5：直接关闭应用
//		Thread.sleep(2000);
//		driver.closeApp();
//		无
//		无
		
//		3:启动应用
//		Thread.sleep(2000);
//		driver.launchApp();
		//		无
//		无
		
//		4：将应用退出到后台
//		Thread.sleep(2000);
//		driver.runAppInBackground(Duration.ofSeconds(5L));
//		退出到后台的时间
//		无
		
//		6：重置应用程序
//		Thread.sleep(2000);
//		driver.resetApp();
//		无
//		无
		
//		7：移除应用
//		driver.removeApp(bundleId);
//		System.out.println(driver.isAppInstalled(bundleId));
//		App的bundleId
//		true表示移除成功
		
//		9：退出应用
//		Thread.sleep(2000);
//		driver.terminateApp(bundleId);
//		App的bundleId
		
//		8：激活应用
//		Thread.sleep(2000);
//		driver.activateApp(bundleId);
//		App的bundleId
//		无
//		正在运行的App成功退出返回true
		
//		10：查看应用状态
//		ApplicationState state = driver.queryAppState(bundleId);
//		System.out.println(state);
//		App的bundleId
//		ApplicationState，如NOT_RUNNING

//		Thread.sleep(3000);
//		driver.quit();

	}

}
