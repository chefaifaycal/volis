import { Text, View } from 'react-native';

import { useTheme } from '@/theme';

import { Icon, type IconName } from './Icon';

export function Card({ icon, title, subtitle, meta }: { icon: IconName; title: string; subtitle?: string; meta?: string }) {
  const t = useTheme();
  return (
    <View
      style={{
        flexDirection: 'row',
        gap: t.space['1.5'],
        padding: t.space['2'],
        borderRadius: t.radii.lg,
        borderWidth: 1.5,
        borderColor: t.colors.borderSubtle,
        backgroundColor: t.colors.surface,
        minHeight: t.layout.minTouch,
      }}>
      <Icon name={icon} size={22} color={t.colors.primary} />
      <View style={{ flex: 1, gap: t.space['0.5'] }}>
        <Text style={[t.typography.title, { color: t.colors.text }]}>{title}</Text>
        {subtitle ? <Text style={[t.typography.bodySm, { color: t.colors.textSecondary }]}>{subtitle}</Text> : null}
        {meta ? <Text style={[t.typography.caption, { color: t.colors.primaryPressed }]}>{meta}</Text> : null}
      </View>
    </View>
  );
}
