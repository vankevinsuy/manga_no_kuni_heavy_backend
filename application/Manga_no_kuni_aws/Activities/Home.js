import React, { useState } from 'react';
import { StyleSheet,  StatusBar, Text, View} from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';

// themes import 
import * as light_theme from '../assets/themes/light';
import * as dark_theme from '../assets/themes/dark';
import * as app_common_style from '../assets/themes/common_style';
import { getTheme } from '../CustomFunctions/CommonVariable';

// components import 
import HeaderSearch from '../components/Header_search';
import { Value } from 'react-native-reanimated';



export default function Home(props) {

  const [DarkSelected, setTheme] = useState();
  function toogleDrawer() {
    props.navigation.openDrawer()
  }

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



  const styles = StyleSheet.create({
    container: {
      flex: 1,
      //alignItems: 'center',
      backgroundColor: (DarkSelected) ? dark_theme.background_color : light_theme.background_color,
    }, 

     txt : {
       color : (DarkSelected) ? dark_theme.text_color : light_theme.text_color,
     }, 

     data : {
       flex : 1,
     }
  });

  return (
    <SafeAreaView style={styles.container}>
      <StatusBar 
        backgroundColor = {(DarkSelected) ? dark_theme.background_color : light_theme.background_color}
        barStyle = {(DarkSelected) ?  'light-content' :  'dark-content'}
      />
      
      <HeaderSearch toogle = {toogleDrawer} dark = {DarkSelected}/>

      
      <View style={styles.data}/>


      <Text style={styles.txt}>Home</Text>

    </SafeAreaView>
  );
}