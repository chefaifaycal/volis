import { useFonts } from 'expo-font';
import Stack from 'expo-router/stack';
import * as SplashScreen from 'expo-splash-screen';
import { StatusBar } from 'expo-status-bar';
import { useEffect } from 'react';
import { SafeAreaProvider } from 'react-native-safe-area-context';

import { fontAssets, useTheme } from '@/theme';

SplashScreen.preventAutoHideAsync();

// Fournisseurs globaux (thème, polices). À compléter : i18n, session, requêtes (TanStack Query).
export default function RootLayout() {
  const t = useTheme();
  const [loaded, error] = useFonts(fontAssets);

  useEffect(() => {
    if (loaded || error) SplashScreen.hideAsync();
  }, [loaded, error]);

  if (!loaded && !error) return null;

  return (
    <SafeAreaProvider>
      <StatusBar style={t.scheme === 'dark' ? 'light' : 'dark'} />
      <Stack screenOptions={{ headerShown: false, contentStyle: { backgroundColor: t.colors.bg } }} />
    </SafeAreaProvider>
  );
}
