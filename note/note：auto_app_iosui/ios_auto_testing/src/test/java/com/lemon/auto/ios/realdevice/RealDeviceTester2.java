package com.lemon.auto.ios.realdevice;

import java.net.URL;
import java.util.List;

import org.openqa.selenium.By;
import org.openqa.selenium.remote.DesiredCapabilities;

import io.appium.java_client.MobileBy;
import io.appium.java_client.ios.IOSDriver;
import io.appium.java_client.ios.IOSElement;
import io.appium.java_client.remote.MobileCapabilityType;

/**
 * {
  "platformName": "iOS",
  "deviceName": "iPhone",
  "platformVersion": "11.4.1",
  "bundleId": "com.lemonban.UICatalog2",
  "udid": "1dc2260025f1574c95470b783b6b99fb0f3cbf08",
  "xcodeOrgId": "M87SUKS9QG",
  "xcodeSigningId": "iPhone Developer"
}
用的是付费的开发者账号，找开发人员去要
 * @author happy
 *
 */
public class RealDeviceTester2 {
	public static void main(String[] args) throws Exception {
		// 期望的能力对象
		DesiredCapabilities desiredCapabilities = new DesiredCapabilities();
		desiredCapabilities.setCapability(MobileCapabilityType.PLATFORM_NAME, "iOS");// 平台名
		desiredCapabilities.setCapability("platformVersion", "11.4.1");// 平台版本
//		desiredCapabilities.setCapability("bundleId", "com.lemonban.UICatalog2");// app文件的路径
		desiredCapabilities.setCapability("app", "/Users/happy/Desktop/tools/app/UICatalog.ipa");// app文件的路径
		desiredCapabilities.setCapability("deviceName", "iPhone");// 设备名
		desiredCapabilities.setCapability(MobileCapabilityType.UDID, "1dc2260025f1574c95470b783b6b99fb0f3cbf08");
		desiredCapabilities.setCapability("xcodeOrgId", "9N685V2QM7");
		desiredCapabilities.setCapability("xcodeSigningId", "iPhone Developer");
		

		URL remoteAddress = new URL("http://localhost:4723/wd/hub");
		
		IOSDriver<IOSElement> driver = new IOSDriver<IOSElement>(remoteAddress, desiredCapabilities);
		
		driver.findElementByAccessibilityId("id_cell_action_sheet").click();

		Thread.sleep(3000);
		driver.quit();

	}

}
