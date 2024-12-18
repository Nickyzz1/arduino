// import React, { useEffect, useState } from 'react';
// import { View, Text } from 'react-native';
// import firestore from '@react-native-firebase/firestore';

// const App = () => {
//   const [location, setLocation] = useState(null);

//   useEffect(() => {
//     const unsubscribe = firestore()
//       .collection('gps_data')
//       .doc('robo_carga')
//       .onSnapshot(documentSnapshot => {
//         const data = documentSnapshot.data();
//         setLocation(data);
//       });

//     return () => unsubscribe(); // Limpar o ouvinte quando o componente for desmontado
//   }, []);

//   return (
//     <View>
//       <Text>Localização do Robô:</Text>
//       {location ? (
//         <Text>Latitude: {location.latitude}, Longitude: {location.longitude}</Text>
//       ) : (
//         <Text>Esperando dados...</Text>
//       )}
//     </View>
//   );
// };

// export default App;
