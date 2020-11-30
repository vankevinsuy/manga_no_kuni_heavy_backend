import React, { useState } from 'react';
import { Image, StyleSheet, Button, StatusBar, Text } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';

// themes import 
import * as light_theme from '../assets/themes/light';
import * as dark_theme from '../assets/themes/dark';
import * as app_common_style from '../assets/themes/common_style';
import { changeTheme, getTheme } from '../CustomFunctions/CommonVariable';

// import components
import Header from '../components/Header';

export default function Favoris(props) {

  const [DarkSelected, setTheme] = useState();

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


  const styles = StyleSheet.create({
    container: {
      flex: 1,
      backgroundColor: (DarkSelected) ? dark_theme.background_color : light_theme.background_color,
    }, 

     txt : {
       color : "white"
     }
  });

  return (
    <SafeAreaView style={styles.container}>
      <StatusBar 
        backgroundColor = {(DarkSelected) ? dark_theme.background_color : light_theme.background_color}
        barStyle = {(DarkSelected) ?  'light-content' :  'dark-content'}
      />

<Header toogle = {toogleDrawer} dark = {DarkSelected}/>
      <Text style={styles.txt}>Favoris</Text>

    </SafeAreaView>
  );
}