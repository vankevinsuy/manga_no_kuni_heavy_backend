import React, {useState} from "react";
import { StyleSheet, View , Image, Text, Switch} from 'react-native';
import AsyncStorage from '@react-native-async-storage/async-storage';


import * as light_theme from '../assets/themes/light';
import * as dark_theme from '../assets/themes/dark';
import * as app_common_style from '../assets/themes/common_style';
import * as commonFunc from '../Common_functions';


import PseudoTextInput from '../components/pseudo_text_input';
import PasswordTextInput from '../components/password_text_input';
import SingninButton from  '../components/signin_button';
import SingnupButton from  '../components/signup_button';

 


const ConnectionInscription = (navigation) => {

  commonFunc.androidQuit();

  const [DarkSelected, setIsEnabled] = useState(commonFunc.getTheme());
  const toggleSwitch = async () => {
    setIsEnabled(previousState => !previousState);

    if(DarkSelected) {
      await AsyncStorage.setItem('theme', "dark");
    }
    else{
      await AsyncStorage.setItem('theme', "light");
    }
  };

  const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor : (DarkSelected) ? dark_theme.background_color : light_theme.background_color,
    }, 
  
    banner: {
        flex: 1,
        justifyContent: "center",
        alignItems: "center",
    }, 
  
    form_container: {
        flex: 1,
    }, 
  
    text : {
      fontSize : 15,
      alignSelf : "center",
      color :  (DarkSelected) ? dark_theme.text_color : light_theme.text_color
    }
  });

    return (
      <View style={styles.container}>
            <Image
                style={styles.banner}
                source= {(DarkSelected) ? require('../assets/app_images/banner_dark.png') :  require('../assets/app_images/banner_light.png')}
            />

            <View style={styles.form_container}>
                <PseudoTextInput darkSelected = {DarkSelected}/>
                <PasswordTextInput  darkSelected = {DarkSelected}/>
                <SingnupButton/>

                <Text style={styles.text}>Already have an account</Text>

                <SingninButton/>
            </View>

          <View style={app_common_style.switch_theme_style}>
              <Text style = {styles.text}>Light</Text>
              <Switch
                trackColor={{ false: app_common_style.switch_trackColor_false, true: app_common_style.switch_trackColor_true }}
                thumbColor={DarkSelected ? app_common_style.switch_thumbColor_true : app_common_style.switch_thumbColor_false}
                ios_backgroundColor= {app_common_style.switch_trackColor_false}
                onValueChange={toggleSwitch}
                value={DarkSelected}
              />
              <Text style = {styles.text} >Dark</Text>
          </View>

      </View>
    );
}





export default ConnectionInscription;