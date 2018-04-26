// Team Name: Charity (Kimberly Atienza, Joesph Bingham, Keith Horace, Darren Johnson, Ryan Parker, Alexander Partain, Emiley Smith, Kenton Wilhelm)
// Date: 4/25/18
// Assignment: TIMELOCK

// compile in linux:  "javac TimelockFinal.java"
// run in linux: "java TimelockFinal < epoch.txt"
//		where epoch.txt has the epoch date in it

import java.util.*;
import java.text.*;
import java.security.*;
import javax.xml.bind.DatatypeConverter;
import java.math.*;
import java.io.*;
import java.time.*;
class TimelockFinal
{ 
	public static void main(String [] args)
	{
		//get the epoch time from txt file
		Scanner sc = new Scanner(System.in);
		String line = sc.nextLine();
		
		//initialize date format and different times to keep track of
		TimeZone.setDefault(TimeZone.getTimeZone("UTC"));
		SimpleDateFormat dateParser = new SimpleDateFormat("yyyy MM dd HH mm ss");
		Calendar systemTime = Calendar.getInstance();
		Calendar epochTime = Calendar.getInstance();
		
		
		//set the epoch time, the system time was automatically set when creating the Calendar objects above
		try{
			dateParser.setTimeZone(TimeZone.getTimeZone("UTC"));
			epochTime.setTime(dateParser.parse(line));
		}catch(ParseException e){
			System.out.println("error parsing");
		}
		
		//set the system seconds to line up with the epoch seconds
		//zero out the system milliseconds, we don't need them
		systemTime.set(systemTime.MILLISECOND,0);
		

		//getTimeCode takes the two times, finds the difference in seconds, and then spits out the timeCode
		// this is done 3 times.
		getTimeCode(systemTime, epochTime);
		
	}
	
	public static String md5Hash(String hash){
		try{
			MessageDigest md5 = MessageDigest.getInstance("MD5");
			md5.update(hash.getBytes("UTF-8"));
			return String.format("%032x", new BigInteger(1, md5.digest()));
		}
		catch(NoSuchAlgorithmException e){		
			
		}
		catch(UnsupportedEncodingException e){
			
		}
		
		return "";
	}
	
	public static String letterCode(String hash){
		
		int j = 0;
		String timeCode = "";
		for(int i = 0; i < hash.length()-1; i++ ){
			
			if(Character.isAlphabetic(hash.charAt(i))){
				timeCode += hash.charAt(i);
				j++;
			}
			
			if(j == 2){
				return timeCode;
			}
			
		}
		
		return "ee";
	}
	
	public static String numCode(String hash){
		
		int j = 0;
		String timeCode = "";
		for(int i = 0; i < hash.length()-1; i++ ){
			
			if(!(Character.isAlphabetic(hash.charAt(hash.length()-1-i)))){
				timeCode += hash.charAt(hash.length()-1-i);
				j++;
			}
			
			if(j == 2){
				return timeCode;
			}
			
		}
		
		return "12";
	}
	
	public static void getTimeCode(Calendar systemTime, Calendar epochTime){
		
		
		if(TimeZone.getTimeZone("US/Central").inDaylightTime(systemTime.getTime())){
			int currentHour = systemTime.get(systemTime.HOUR_OF_DAY);
			systemTime.set(systemTime.HOUR_OF_DAY, currentHour-1);
		}
		
		if(TimeZone.getTimeZone("US/Central").inDaylightTime(epochTime.getTime())){
			int currentHour = epochTime.get(epochTime.HOUR_OF_DAY);
			epochTime.set(epochTime.HOUR_OF_DAY, currentHour-1);
		}
		
		long systemSeconds = systemTime.get(systemTime.SECOND);
		long timeAfterEpochRaw = ((systemTime.getTimeInMillis()-epochTime.getTimeInMillis())/(1000));
		long timeAfterEpoch = timeAfterEpochRaw -(timeAfterEpochRaw%60);	
		
		
		String holyHash = md5Hash(md5Hash(Long.toString(timeAfterEpoch)));
		String timeCode = "";
		
		timeCode += letterCode(holyHash);
		timeCode += numCode(holyHash);
		SimpleDateFormat dateParser = new SimpleDateFormat("yyyy MM dd HH mm ss");
		
			System.out.println(timeCode);
	}

}