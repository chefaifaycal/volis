import { AsyncList } from '@/ui/components/AsyncList';
import { Screen } from '@/ui/components/Screen';
import { useMessagesViewModel } from '@/ui/viewmodels';

export function MessagesScreen() {
  const state = useMessagesViewModel();
  return (
    <Screen title="Messages">
      <AsyncList state={state} icon="message" empty="Aucune conversation." />
    </Screen>
  );
}
