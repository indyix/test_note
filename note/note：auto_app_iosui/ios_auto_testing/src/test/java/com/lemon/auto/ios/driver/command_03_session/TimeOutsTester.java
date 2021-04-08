package com.lemon.auto.ios.driver.command_03_session;

import java.io.File;
import java.net.URL;
import java.util.Map;
import java.util.concurrent.TimeUnit;

import org.apache.commons.io.FileUtils;
import org.openqa.selenium.By;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import io.appium.java_client.functions.ExpectedCondition;
import io.appium.java_client.ios.IOSDriver;
import io.appium.java_client.ios.IOSElement;

public class TimeOutsTester {
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

		//1:硬性等待、线程等待、线程休眠
//		Thread.sleep(3000);
//		driver.findElement(By.id("id_cell_action_sheet")).click();
		
		
		//2:隐式等待:全局  DOM结构
//		driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
//		driver.findElement(By.id("id_cell_action_sheet_6666")).click();
		
		//3:显式等待、智能等待:推荐使用，不会浪费时间
		WebDriverWait wait = new WebDriverWait(driver, 10);
//		IOSElement element = wait.until(new ExpectedCondition<IOSElement>() {
//			@Override
//			public IOSElement apply(WebDriver input) {
//				System.out.println("-------------------------");
//				return driver.findElement(By.id("id_cell_action_sheet_6666"));
//			}
//		});
//		element.click();
		
		WebElement element = wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("id_cell_action_sheet")));
		element.click();
		
		Thread.sleep(3000);
		driver.quit();

	}

}
