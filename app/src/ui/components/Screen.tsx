import type { ReactNode } from 'react';
import { ScrollView, Text, View } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';

import { useTheme } from '@/theme';

export function Screen({ title, subtitle, children }: { title: string; subtitle?: string; children?: ReactNode }) {
  const t = useTheme();
  return (
    <SafeAreaView style={{ flex: 1, backgroundColor: t.colors.bg }} edges={['top']}>
      <ScrollView contentContainerStyle={{ padding: t.layout.screenMargin, gap: t.space['2'] }}>
        <View style={{ gap: t.space['0.5'] }}>
          <Text accessibilityRole="header" style={[t.typography.h1, { color: t.colors.text }]}>
            {title}
          </Text>
          {subtitle ? (
            <Text style={[t.typography.body, { color: t.colors.textSecondary }]}>{subtitle}</Text>
          ) : null}
        </View>
        {children}
      </ScrollView>
    </SafeAreaView>
  );
}
