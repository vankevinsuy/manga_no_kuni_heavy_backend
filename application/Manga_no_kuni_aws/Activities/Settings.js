import React, { useState } from 'react';
import { StyleSheet, Button, StatusBar, Text, View, Switch } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';

import { Auth } from 'aws-amplify';

// themes import 
import * as light_theme from '../assets/themes/light';
import * as dark_theme from '../assets/themes/dark';
import * as app_common_style from '../assets/themes/common_style';
import { changeTheme, getTheme } from '../CustomFunctions/CommonVariable';

// import components
import Header from '../components/Header';

export default function Settings(props) {
  async function signOut() {
    try {
      await Auth.signOut();
      props.updateAuthState('loggedOut');
    } catch (error) {
      console.log('Error signing out: ', error);
    }
  }

  const [DarkSelected, setTheme] = useState();
  const [themeGet, setGetted] = useState(false);

  // set DarkSelected state value
  getTheme().then((value) => {
    console.log("Singin theme " + value);

    if(value === "dark"){
      setTheme(true);
      console.log("DarkSelected = " + DarkSelected);
    }
    if(value === "light"){
      setTheme(false);
      console.log("DarkSelected = " + DarkSelected);
    }
  });
  function toogleDrawer() {
    props.navigation.openDrawer()
  }

  const toggleSwitch = async () => {

    setTheme(previousState => !previousState);    
    setGetted(true);

    if(!DarkSelected === true){
      changeTheme("dark");
    }
    else{
      changeTheme("light");
    }
  };


  const styles = StyleSheet.create({
    container: {
      flex: 1,
      backgroundColor: (DarkSelected) ? dark_theme.background_color : light_theme.background_color,
    }, 

     text : {
       color : (DarkSelected) ? dark_theme.text_color : light_theme.text_color,
     }
  });

  return (
    <SafeAreaView style={styles.container}>
      <StatusBar 
        backgroundColor = {(DarkSelected) ? dark_theme.background_color : light_theme.background_color}
        barStyle = {(DarkSelected) ?  'light-content' :  'dark-content'}
      />
      <Header toogle = {toogleDrawer} dark = {DarkSelected}/>
      <Text style={styles.text}>Settings</Text>
      <Button title="Sign Out" color="tomato" onPress={signOut} />

      
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

    </SafeAreaView>
  );
}