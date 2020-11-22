import React from 'react';
import { StyleSheet, View , Image} from 'react-native';
import * as app_color from '../assets/themes/common_style';
import AsyncStorage from '@react-native-async-storage/async-storage';


const defineActivity = (navigation) =>{
    setTimeout(async () => {
        try {
            const pseudo = await AsyncStorage.getItem('pseudo');
            console.log("pseudo = " + pseudo + " Activity = SplashScreen");
    
            if(pseudo !== null) {
                navigation.navigate("ConnectionInscription"); // home
            }
            else{
                navigation.navigate("ConnectionInscription");
            }
        } 
        catch(e) {
            console.log(e);
        }
    }, 2000)

};

const SplashScreen = ({ navigation }) =>  {
    defineActivity(navigation);
    return (
      <View style={styles.container}>
            <Image
                style={styles.logo}
                source={require('../assets/app_images/logo.png')}
            />
      </View>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: "center",
        alignItems: "center",
        backgroundColor : app_color.splash_screen_color
    },
    logo : {
        height : 400,
        width : 400,
        resizeMode : "center",
        justifyContent: "center",
        alignItems: "center",
    }
});

export default SplashScreen;