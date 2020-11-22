import { useEffect } from "react";
import {BackHandler, Alert} from 'react-native';
import AsyncStorage from '@react-native-async-storage/async-storage';


export function androidQuit(){
  useEffect(() => {
    const backAction = () => {
      Alert.alert("Hold on!", "Are you sure you want to quit ?", [
        {
          text: "Cancel",
          onPress: () => null,
          style: "cancel"
        },
        { text: "YES", onPress: () => BackHandler.exitApp() }
      ]);
      return true;
    };
  
    const backHandler = BackHandler.addEventListener(
      "hardwareBackPress",
      backAction
    );
  
    return () => backHandler.remove();
  }, []);
};

export const getTheme = async () => {
  try {
    const Darked = await AsyncStorage.getItem('theme');

    if(Darked == null) {
      await AsyncStorage.setItem('theme', "light");
    }

    if (Darked === "dark"){
      console.log("themeaaa = "  + Darked);
      return true;
    }
    if (Darked === "light"){
      console.log("theme = "  + Darked);
      return false;
    }
  } 
  catch(e) {
    console.error(e);
  }
};