import React, { useEffect, useState } from 'react';
import Chip from '@material-ui/core/Chip';
import {API_SERVER} from './settings.js';
import {
  SafeAreaView,
  StyleSheet,
  ScrollView,
  View,
  Text,
  StatusBar,
} from 'react-native';

const App: () => React$Node = () => {
  const  [hasError, setErrors] =  useState(false);
  const  [planets,setPlanets ]= useState({});

  async function fetchData() {
    const res = await fetch(`${API_SERVER}/thingaroo`);
    res
      .json()
      .then(res => setPlanets(res))
      .catch(err => setErrors(err));
  }

  useEffect(() => {
    fetchData();
  }, [])

  return (
    <>
      <StatusBar barStyle="dark-content" />
      <SafeAreaView>
        <ScrollView
          contentInsetAdjustmentBehavior="automatic"
          style={styles.scrollView}>
          {global.HermesInternal == null ? null : (
            <View style={styles.engine}>
              <Text style={styles.footer}>Engine: Hermes</Text>
            </View>
          )}
          <View style={styles.body}>
            <View style={styles.sectionContainer}>
              <Text style={styles.sectionTitle}>Testing text here:</Text>
              <Text style={styles.sectionDescription}>
                Super text!
              </Text>
            </View>
            <View style={styles.sectionContainer}>
              <Text style={styles.sectionTitle}>ThingaRoos:</Text>
              <Text style={styles.sectionDescription}>
                {JSON.stringify(planets)}
              </Text>
            </View>            
            {/* <View style={styles.sectionContainer}>
              <Text style={styles.sectionTitle}>Thingaroos:</Text>
              <Chip
                label="This"
                color="primary"
              />
            </View> */}
          </View>
        </ScrollView>
      </SafeAreaView>
    </>
  );
};

const styles = StyleSheet.create({
  engine: {
    position: 'absolute',
    right: 0,
  },
  sectionContainer: {
    marginTop: 32,
    paddingHorizontal: 24,
  },
  sectionTitle: {
    fontSize: 24,
    fontWeight: '600',
  },
  sectionDescription: {
    marginTop: 8,
    fontSize: 18,
    fontWeight: '400',
  },
  highlight: {
    fontWeight: '700',
  },
  footer: {
    fontSize: 12,
    fontWeight: '600',
    padding: 4,
    paddingRight: 12,
    textAlign: 'right',
  },
  chips: {
    display: 'flex',
    justifyContent: 'center',
    flexWrap: 'wrap',
    margin: 2,
  },
});

export default App;
