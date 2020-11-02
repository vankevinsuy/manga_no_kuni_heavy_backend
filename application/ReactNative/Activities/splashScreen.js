import React, { Component } from 'react';
import { StyleSheet,Text, View , Image} from 'react-native';

class SplashScreen extends Component {
  render() {
    return (
      <View style={styles.container}>
            <Image
                style={styles.logo}
                source={require('../assets/logo.png')}
            />
      </View>
    );
  }
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: "center",
        alignItems: "center",
        backgroundColor : "#ff9300"
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