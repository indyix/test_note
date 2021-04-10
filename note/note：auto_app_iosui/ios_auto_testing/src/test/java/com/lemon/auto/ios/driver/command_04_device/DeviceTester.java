package com.lemon.auto.ios.driver.command_04_device;

import java.net.URL;
import java.util.Map;

import org.openqa.selenium.ScreenOrientation;
import org.openqa.selenium.remote.DesiredCapabilities;

import io.appium.java_client.ios.IOSDriver;
import io.appium.java_client.ios.IOSElement;

public class DeviceTester {
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
		
		driver.rotate(ScreenOrientation.PORTRAIT);
		//1:抖动
//		driver.shake();
		
//		2:锁定设备 
		System.out.println(driver.isDeviceLocked());
		Thread.sleep(2000);
		driver.lockDevice();
//		3:解锁设备 
		System.out.println(driver.isDeviceLocked());
		Thread.sleep(3000);
		driver.unlockDevice();
//		4:检查设备是否锁定 
		Boolean isDeviceLocked = driver.isDeviceLocked();
		System.out.println(isDeviceLocked);

		Thread.sleep(3000);
		driver.quit();

	}

}
