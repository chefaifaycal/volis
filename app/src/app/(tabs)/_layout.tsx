import { Tabs } from 'expo-router/js-tabs';

import { useTheme } from '@/theme';
import { Icon, type IconName } from '@/ui/components/Icon';

const tabs: readonly { name: string; title: string; icon: IconName }[] = [
  { name: 'index', title: 'Accueil', icon: 'home' },
  { name: 'envois', title: 'Envois', icon: 'package' },
  { name: 'voyages', title: 'Voyages', icon: 'plane' },
  { name: 'messages', title: 'Messages', icon: 'message' },
  { name: 'profil', title: 'Profil', icon: 'user' },
];

export default function TabsLayout() {
  const t = useTheme();
  return (
    <Tabs
      screenOptions={{
        headerShown: false,
        tabBarActiveTintColor: t.colors.primary,
        tabBarInactiveTintColor: t.colors.textMuted,
        tabBarLabelStyle: t.typography.tab,
        tabBarStyle: { backgroundColor: t.colors.surface, borderTopColor: t.colors.borderSubtle },
      }}>
      {tabs.map((tab) => (
        <Tabs.Screen
          key={tab.name}
          name={tab.name}
          options={{
            title: tab.title,
            tabBarIcon: ({ color, size }) => <Icon name={tab.icon} color={color} size={size} />,
          }}
        />
      ))}
    </Tabs>
  );
}
