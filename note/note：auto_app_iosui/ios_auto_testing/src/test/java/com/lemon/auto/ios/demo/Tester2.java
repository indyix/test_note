package com.lemon.auto.ios.demo;

import java.net.URL;

import org.openqa.selenium.By;
import org.openqa.selenium.remote.DesiredCapabilities;

import io.appium.java_client.ios.IOSDriver;
import io.appium.java_client.ios.IOSElement;

public class Tester2 {

	public static void main(String[] args) throws Exception {
		//期望的能力对象
		DesiredCapabilities desiredCapabilities = new DesiredCapabilities();
		desiredCapabilities.setCapability("platformName", "iOS");//平台名
		desiredCapabilities.setCapability("platformVersion", "13.1");//平台版本
		desiredCapabilities.setCapability("app", "/Users/nick/Desktop/tools/app/UICatalog.app");//app文件的路径
		desiredCapabilities.setCapability("deviceName", "iPhone 8");//设备名

		//打开模拟器（iOS设备）
		//打开app
		URL remoteAddress = new URL("http://localhost:4723/wd/hub");
		IOSDriver<IOSElement> driver = new IOSDriver<IOSElement>(remoteAddress, desiredCapabilities);
		Thread.sleep(3000);
		//元素定位和操作
		driver.findElement(By.id("id_cell_action_sheet")).click();
		
		Thread.sleep(3000);
		driver.quit();
		
	}

}
